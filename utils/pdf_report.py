from reportlab.platypus import SimpleDocTemplate, Table

def create_pdf(data):

    pdf = SimpleDocTemplate("reports/report.pdf")

    rows = [["Review","Sentiment","Score"]]

    for d in data:
        rows.append([
            d["text"],
            d["sentiment"],
            str(round(d["score"],2))
        ])

    table = Table(rows)

    pdf.build([table])