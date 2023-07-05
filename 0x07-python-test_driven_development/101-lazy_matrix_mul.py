#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Arguments:
    m_a -- a numpy ndarray representing Matrix A
    m_b -- a numpy ndarray representing Matrix B

    Returns:
    result -- a numpy ndarray representing the result of matrix multiplication (m_a * m_b)

    """
    return (np.matmul(m_a, m_b))
