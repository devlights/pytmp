"""
工務端末が出力した電文ダンプファイルを削除します。

usage::
  $ python remove_dump_telegrams.py [TARGET_DIRECTORY]
"""
import argparse
import pathlib


def delete(target_dir: str, suffix: str = 'bin') -> None:
    """
    指定ディレクトリ下の電文ダンプファイルを削除します。
    ディレクトリを再帰で処理はしません。指定したディレクトリ直下のみが処理対象になります。

    :param target_dir: 対象ディレクトリ
    :param suffix: 対象拡張子
    :return: なし
    """
    p = pathlib.Path(target_dir)

    if not p.exists():
        raise NotADirectoryError('specify the target directory.')

    for item in p.glob(f'*.{suffix}'):
        if item.name.startswith(('Send', 'Recv')):
            item.unlink()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--target-directory',
                        dest='target_directory',
                        default='/Mdcs/MdcsApp/Bin',
                        nargs='?',
                        type=str,
                        help='対象ディレクトリ')

    args = parser.parse_args()
    delete(args.target_directory)
