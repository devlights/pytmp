"""
工務端末が出力した電文ダンプファイルをフォルダ構造にパッキングします。
生成されるディレクトリ構造は以下のようになります。

directory structure::
/Mdcs/MdcsApp/Bin/DumpTelegrams
                            /Send
                            /Recv

usage::
  $ python pack_dump_telegrams.py [TARGET_DIRECTORY]
"""
import argparse
import os
import pathlib
import shutil


def pack(target_dir: str, suffix: str = 'bin') -> None:
    """
    指定ディレクトリ下の電文ダンプファイルをパッキングします。
    ディレクトリを再帰で処理はしません。指定したディレクトリ直下のみが処理対象になります。

    :param target_dir: 対象ディレクトリ
    :param suffix: 対象拡張子
    :return: なし
    """
    p = pathlib.Path(target_dir)

    if not p.exists():
        raise NotADirectoryError('specify the target directory.')

    os.makedirs(f'{target_dir}/DumpTelegrams/Send', exist_ok=True)
    os.makedirs(f'{target_dir}/DumpTelegrams/Recv', exist_ok=True)

    send_telegrams = []
    recv_telegrams = []
    for item in p.glob(f'*.{suffix}'):
        name = item.name
        if name.startswith('Send'):
            send_telegrams.append(item)
        elif name.startswith('Recv'):
            recv_telegrams.append(item)

    for item in send_telegrams:
        shutil.move(item.absolute(), f'{target_dir}/DumpTelegrams/Send/{item.name}')
    for item in recv_telegrams:
        shutil.move(item.absolute(), f'{target_dir}/DumpTelegrams/Recv/{item.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--target-directory',
                        dest='target_directory',
                        default='/Mdcs/MdcsApp/Bin',
                        nargs='?',
                        type=str,
                        help='対象ディレクトリ')

    args = parser.parse_args()
    pack(args.target_directory)
