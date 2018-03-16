"""
工務端末が出力したログファイルを削除します。

usage::
  $ python remove_log_files.py [TARGET_DIRECTORY]
"""
import pathlib

import click


def delete(target_dir: str, prefix: str = 'Mdcs') -> None:
    """
    指定された条件に合致したファイルを削除します。

    :param target_dir: 対象ディレクトリ
    :param prefix: ファイル名プレフィックス
    :return: なし
    """
    p = pathlib.Path(target_dir)

    if not p.exists():
        click.echo(f'directory not found {p}')
        raise NotADirectoryError('specify the target directory.')

    for item in p.glob(f'{prefix}*'):  # type: pathlib.Path
        item.unlink()


@click.command()
@click.option('--target-dir', type=str, default='/Mdcs/AppData/AppLog', help='対象ディレクトリ')  # noqa: E501
@click.option('--prefix', type=str, default='Mdcs', help='ファイル名のプレフィックス')
def main(target_dir: str, prefix: str = 'Mdcs') -> None:
    """工務端末のログファイルを削除します。"""
    delete(target_dir, prefix)


if __name__ == '__main__':
    main()
