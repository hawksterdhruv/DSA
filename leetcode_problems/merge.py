import logging
from commons.my_logging import logger

logger.setLevel(logging.INFO)


class K:
    @staticmethod
    def merge_without_duplicates(l1, l2):
        m, n = len(l1), len(l2)
        logger.debug("merge : (%s,%s)", m, n)
        i, j = 0, 0
        op = []
        while i < m and j < n:
            if l1[i] < l2[j]:
                op.append(l1[i])
                i += 1
            elif l1[i] > l2[j]:
                op.append(l2[j])
                j += 1
            else:
                op.append(l2[j])
                i += 1
                j += 1

        if i == m:
            op += l2[j:]
        else:
            op += l1[i:]
        return op


if __name__ == "__main__":
    res = K.merge_without_duplicates([1, 4], [1, 2, 3])
    print(res)
