# ============================================================================
# 付録 A 機器の性能を表す仕様の決定方法
# ============================================================================

import jjjexperiment.constants as constants

# ============================================================================
# A.2 定格能力
# ============================================================================

# 定格暖房能力 (1)
def get_q_rtd_H(q_rtd_C):
    """定格暖房能力 (1)

    Args:
      q_rtd_C(float): 定格冷房能力(W)

    Returns:
      float: 定格暖房能力 (1)

    """
    return 1.2090 * q_rtd_C - 85.1


# 定格冷房能力 (2)
def get_q_rtd_C(A_HCZ):
    """定格冷房能力 (2)

    Args:
      A_HCZ(float): 暖冷房区画の床面積 (m2)

    Returns:
      float: 定格冷房能力

    """
    q_rtd_C = 190.5 * A_HCZ + 45.6
    return min(constants.q_rtd_C_limit, q_rtd_C)


# ============================================================================
# A.3 最大能力
# ============================================================================

# 最大暖房能力 (3)
def get_q_max_H(q_rtd_H, q_max_C):
    """最大暖房能力 (3)

    Args:
      q_rtd_H(float): 定格暖房能力
      q_max_C(float): 最大冷房能力

    Returns:
      float: 最大暖房能力

    """
    q_max_H = 1.7597 * q_max_C - 413.7
    return max(q_rtd_H, q_max_H)


# 最大冷房能力 (4)
def get_q_max_C(q_rtd_C):
    """最大冷房能力 (4)

    Args:
      q_rtd_C(float): 定格冷房能力

    Returns:
      float: 最大冷房能力

    """
    q_max_C = 0.8462 * q_rtd_C + 1205.9
    return max(q_rtd_C, q_max_C)


# ============================================================================
# A.4 定格エネルギー効率
# ============================================================================

# 定格暖房エネルギー効率 (5)
def get_e_rtd_H(e_rtd_C):
    """定格暖房エネルギー効率 (5)

    Args:
      e_rtd_C(float): 定格冷房エネルギー消費効率

    Returns:
      float: 定格暖房エネルギー効率

    """
    return 0.77 * e_rtd_C + 1.66


# 定格冷房エネルギー効率 (6)
def get_e_rtd_C(e_class, q_rtd_C):
    """定格冷房エネルギー効率 (6)

    Args:
      e_class(str): description]
      q_rtd_C(float): 定格冷房能力

    Returns:
      float: 定格冷房エネルギー効率

    Raises:
      ValueError: e_classが「い」または「ろ」または「は」でない場合に発生する

    """
    if e_class == 'い':
        # (6a)
        return -0.553 * 10 ** (-3) * q_rtd_C + 6.34
    elif e_class == 'ろ':
        # (6b)
        return -0.504 * 10 ** (-3) * q_rtd_C + 5.88
    elif e_class == 'は' or e_class == '不明' or e_class == None:
        # (6c)
        return -0.473 * 10 ** (-3) * q_rtd_C + 5.50
    else:
        raise ValueError(e_class)