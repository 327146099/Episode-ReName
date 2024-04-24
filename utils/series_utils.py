import os
import re


def get_series_from_season_path(season_path):
    """修正系列名称获取 去掉结尾的年份"""
    season_name = os.path.basename(season_path).lower()
    # 如果不是season开头的，提取season开头的名称作为系列名称
    index = season_name.index('season')
    if index != 0:
        return season_name[:index].strip()
    # 取父级目录作为系列名称
    series = os.path.basename(os.path.dirname(season_path))
    pat = '\(\d{4}\)$'
    res = re.search(pat, series)
    if res:
        series = series[:-6].strip()
    return series
