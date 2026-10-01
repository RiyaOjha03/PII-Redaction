def remover_of_pii(redacted_result,test2):
    lst = []
    for r in redacted_result:
        item = test2[r.start:r.end]

        if item in lst:
            continue
        else:
            lst.append(item)

    return (lst)
