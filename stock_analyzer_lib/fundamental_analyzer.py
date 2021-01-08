"""
Extract good company
"""


def company_candidates(all_financial_data):
    ROE_BORDER = 10
    ROA_BORDER = 5

    candidates = []
    for sc in all_financial_data.keys():
        roe = all_financial_data[sc]['ROE']
        roa = all_financial_data[sc]['ROA']
        if roe == None or roa == None:
            continue

        if roe >= ROE_BORDER and roa >= ROA_BORDER:
            candidates.append(sc)

    return candidates