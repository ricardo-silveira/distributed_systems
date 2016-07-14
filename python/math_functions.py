"""
This module implements three mathematical functions to be called by an
RPC-server
"""
import math


def eulerize(num, h=1e-5, base=math.exp(1)):
    """
    This function returns the derivative for `base`**(`num`).
    If `base`= e, it is expected for the derivative to be relatively
    close to `num`.

    Parameters
    ----------
    num (float): point of evaluation of exponential function.
    h (float): interval used for the numerical derivative. Default: 1e-5.
    base (float): base for exponential function. Default: 2.7182... (exp)

    Returns
    -------
    float: derivative value for `base`**(`num`)

    Examples
    --------
    >>> eulerize(3.4)
    29.964249868896783

    >>> eulerize(3.4, 1e-1)
    31.513519112953006

    >>> eulerize(3.4, 1e-1, 2.91)
    42.58638264060849
    """
    if h == 0:
        raise ValueError("Illegal value of h")
    return (base**(num+h)-base**(num))/h


def amp_cosine(frequency, amplitude, t):
    """
    Converts `frequency` from Hz to rad/s and computes its cosine response
    at the given time `t` for the given `amplitude`.

    Parameters
    ----------
    frequency (float): Value in hertz.
    amplitude (float): Value to multiply by the cosine value.
    t (float): time to be evaluated.

    Returns
    -------
    float: A*sin(w*t)

    Examples
    --------
    >>> amp_cosine(0.5, 5, 2)
    -5.0
    """
    return amplitude*math.cos(2*math.pi*frequency*t)


def std_on_the_fly(num, n, mean, delta, m2, variance):
    """
    Computes on-line standard deviation on the fly for number, informing the
    current mean, delta, m2, variance and its n-th position.

    Parameters
    ----------
    num (float): `n`-th number analyzed.
    n (int): number position.
    mean (float): current computed mean value.
    delta (float): current delta computed.
    m2 (float): current m2 computed.
    variance (float): current variance computed.

    Returns
    -------
    float: current standard deviation

    Examples
    --------
    >>> std_on_the_fly(0.15528020654365826,
                       100,
                       -0.28380498874163335,
                       0.43624714539787529,
                       8.3369147369359524,
                       0.08336914736935952)
    0.288737159661
    """
    n += 1
    delta = float(num - mean)
    mean += delta/n
    m2 += delta*(num-mean)
    variance = m2/n
    return math.sqrt(variance)
