# ============================================================================

# 付録 B 機器の性能を表す仕様の決定方法
# ============================================================================

import jjjexperiment.constants as constants
from jjjexperiment.constants import PROCESS_TYPE_3

# ============================================================================
# B.2 熱源機
# ============================================================================

# ============================================================================
# B.2.1 定格能力および定格消費電量
# ============================================================================

# 定格暖房能力[W]  (1)
def get_q_hs_rtd_H(region, A_A):
    """

    Args:
      region: param A_A:
      A_A: 

    Returns:

    """
    q_rq_H = get_q_rq_H(region)
    f_CT = get_f_CT()
    f_CL = get_f_CL()

    return q_rq_H * A_A * f_CT * f_CL  # (1)

    return C_pl_H * C_DL

# 定格冷房能力[W]  (2)
def get_q_hs_rtd_C(region, A_A):
    """

    Args:
      region: param A_A:
      A_A: 

    Returns:

    """
    q_rq_C = get_q_rq_C(region)
    f_CT = get_f_CT()
    f_CL = get_f_CL()

    return q_rq_C * A_A * f_CT * f_CL  # (2)


# 単位面積当たりの必要暖房能力
def get_q_rq_H(region):
    """

    Args:
      region: 

    Returns:

    """
    return table_1[0][region - 1]


# 単位面積当たりの必要冷房能力
def get_q_rq_C(region):
    """

    Args:
      region: 

    Returns:

    """
    return table_1[1][region - 1]


# 外気温度能力補正係数
def get_f_CT():
    """ """
    return 1.05


# 間歇運転能力補正係数
def get_f_CL():
    """ """
    return 1.0

# 表1 単位面積当たりの必要暖房能力及び冷房能力（W/m2)
table_1 = [
    (73.91, 64.32, 62.65, 66.99, 72.64, 61.34, 64.55, 00.00),
    (37.61, 36.55, 42.34, 54.08, 61.69, 60.79, 72.53, 61.56)
]


# 定格暖房消費電力 [W] (3)
def get_P_hs_rtd_H(q_rtd_H):
    """

    Args:
      q_rtd_H: 定格暖房能力 [W]

    Returns:
      定格暖房消費電力 [W]

    """
    e_rtd_H = get_e_rtd_H()
    return q_rtd_H / e_rtd_H  # (3)


# 定格冷房消費電力 [W] (4)
def get_P_hs_rtd_C(q_rtd_C):
    """

    Args:
      q_rtd_C: 定格冷房能力 [W]

    Returns:
      定格冷房消費電力 [W]

    """
    e_rtd_C = get_e_rtd_C()
    return q_rtd_C / e_rtd_C  # (4)


# 定格暖房エネルギー消費効率
def get_e_rtd_H():
    """ """
    return 3.76


# 定格冷房エネルギー消費効率
def get_e_rtd_C():
    """ """
    return 3.17


# ============================================================================
# B.2.2 中間能力および中間消費電力
# ============================================================================

def get_q_hs_mid_H(q_hs_rtd_H):
    """(5)

    Args:
      q_hs_rtd_H: 熱源機の定格暖房能力（W）

    Returns:
      熱源機の中間暖房能力（W）

    """
    return q_hs_rtd_H * 0.5


def get_q_hs_mid_C(q_hs_rtd_C):
    """(6)

    Args:
      q_hs_rtd_C: 熱源機の定格冷房能力（W）

    Returns:
      熱源機の中間冷房能力（W）

    """
    return q_hs_rtd_C * 0.5


# ============================================================================
# B.2.3 最小能力
# ============================================================================

def get_q_hs_min_H(q_hs_rtd_H):
    """(7)

    Args:
      q_hs_rtd_H: 熱源機の定格暖房能力（W）

    Returns:
      熱源機の最小暖房能力（W）

    """
    return q_hs_rtd_H * 0.35


def get_q_hs_min_C(q_hs_rtd_C):
    """(8)

    Args:
      q_hs_rtd_C: 熱源機の定格冷房能力（W）

    Returns:
      熱源機の最小冷房能力（W）

    """
    return q_hs_rtd_C * 0.35


# ============================================================================
# B.3 送風機
# ============================================================================

# ============================================================================
# B.3.1 定格能力運転時の風量および消費電力
# ============================================================================

def get_V_fan_rtd_H(q_hs_rtd_H):
    """(9)

    Args:
      q_hs_rtd_H: 熱源機の定格暖房能力（W）

    Returns:
      定格暖房能力運転時の送風機の風量（m3/h）

    """
    return (1.69 * q_hs_rtd_H * 10 ** (-3) + 14.5) * 60


def get_P_fan_rtd_H(V_fan_rtd_H):
    """(10) ファン消費電力

    Args:
      V_fan_rtd_H: 定格暖房能力運転時の送風機の風量（m3/h）

    Returns:
      定格暖房能力運転時の送風機の消費電力（W）

    """
    return 8.0 * (V_fan_rtd_H / 60) + 20.7


def get_V_fan_rtd_C(q_hs_rtd_C):
    """(11)

    Args:
      q_hs_rdt_C: 熱源機の定格冷房能力（W）

    Returns:
      定格冷房能力運転時の送風機の風量（m3/h）

    """
    return (1.69 * q_hs_rtd_C * 10 ** (-3) + 14.5) * 60


def get_P_fan_rtd_C(V_fan_rtd_C):
    """(12) ファン消費電力

    Args:
      type: 暖房設備機器の種類
      V_fan_rtd_C: 定格冷房能力運転時の送風機の風量（m3/h）
      q_hs_C_d_t: 日付dの時刻tにおける1時間当たりの熱源機の平均冷房能力（W）

    Returns:
      定格冷房能力運転時の送風機の消費電力（W）

    """
    return 8.0 * (V_fan_rtd_C / 60) + 20.7


# ============================================================================
# B.3.2 中間能力運転時の風量および消費電力
# ============================================================================

def get_V_fan_mid_H(q_hs_mid_H):
    """(13)

    Args:
      q_hs_rdt_H: 熱源機の中間暖房能力（W）
      q_hs_mid_H: returns: 中間暖房能力運転時の送風機の風量（m3/h）

    Returns:
      中間暖房能力運転時の送風機の風量（m3/h）

    """
    return (1.69 * q_hs_mid_H * 10 ** (-3) + 14.5) * 60


def get_P_fan_mid_H(V_fan_mid_H):
    """(14)

    Args:
      V_fan_rtd_H: 中間暖房能力運転時の送風機の風量（m3/h）
      V_fan_mid_H: returns: 中間暖房能力運転時の送風機の消費電力（W）

    Returns:
      中間暖房能力運転時の送風機の消費電力（W）

    """
    return 8.0 * (V_fan_mid_H / 60) + 20.7


def get_V_fan_mid_C(q_hs_mid_C):
    """(15)

    Args:
      q_hs_rdt_C: 熱源機の中間冷房能力（W）
      q_hs_mid_C: returns: 中間冷房能力運転時の送風機の風量（m3/h）

    Returns:
      中間冷房能力運転時の送風機の風量（m3/h）

    """
    return (1.69 * q_hs_mid_C * 10 ** (-3) + 14.5) * 60


def get_P_fan_mid_C(V_fan_mid_C):
    """(16)

    Args:
      V_fan_mid_C: 中間冷房能力運転時の送風機の風量（m3/h）

    Returns:
      中間冷房能力運転時の送風機の消費電力（W）

    """
    return 8.0 * (V_fan_mid_C / 60) + 20.7


# ============================================================================
# B.3.3 設計風量
# ============================================================================

def get_V_fan_dsgn_H(V_fan_rtd_H):
    """(17)

    Args:
      V_fan_rtd_H: 定格暖房能力運転時の送風機の風量（m3/h）

    Returns:
      暖房時の送風機の設計風量（m3/h）

    """
    return V_fan_rtd_H * constants.C_V_fan_dsgn_H


def get_V_fan_dsgn_C(V_fan_rtd_C):
    """(18)

    Args:
      V_fan_rtd_C: 定格冷房能力運転時の送風機の風量（m3/h）

    Returns:
      冷房時の送風機の設計風量（m3/h）

    """
    return V_fan_rtd_C * constants.C_V_fan_dsgn_C


# ============================================================================
# 確認用コード
# ============================================================================

