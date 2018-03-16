import collections as col
import glob
import os
import re
import typing as ty

ArtcFile = col.namedtuple('ArtcFile', 'mtime filename')


def _get_artc_files() -> ty.Iterator[str]:
    mtime = os.path.getmtime
    files = (ArtcFile(mtime(x), x) for x in glob.iglob('artc*'))
    return (x.filename for x in sorted(files))


def go():
    os.chdir('/tmp/20180316/1_1から1_3')

    out_set_fp = open('out_set.txt', mode='w', encoding='utf-8')
    out_timeout_fp = open('out_timeout.txt', mode='w', encoding='utf-8')
    out_timerexec_fp = open('out_timerexec.txt', mode='w', encoding='utf-8')

    pat = re.compile(r'.*index:34(?!\d).*')

    with out_set_fp, out_timeout_fp, out_timerexec_fp:
        for f in _get_artc_files():
            with open(f, encoding='euc-jp') as in_fp:
                for line in in_fp:
                    if 'ARTC_10min_rainfall_timeout' in line:
                        if pat.match(line):
                            out_timeout_fp.write(line)
                    if 'ARTC_10min_rainfall_set' in line:
                        if '2100001' in line:
                            out_set_fp.write(line)
                    if 'ARTC_10min_rainfall_timerexec' in line:
                        if pat.match(line):
                            out_timerexec_fp.write(line)


if __name__ == '__main__':
    go()
