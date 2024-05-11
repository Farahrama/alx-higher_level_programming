#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    m_matrix = []
    for row in matrix:
        m_row = []
        for num in row:
            m_row.append(num ** 2)
        m_matrix.append(m_row)
    return m_matrix
