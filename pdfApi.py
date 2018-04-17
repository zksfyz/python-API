# -*- coding: utf-8 -*-

import pdfkit

class HeadlessPdfKit(pdfkit.PDFKit):
    def command(self, path=None):
        return ['xvfb-run', '--'] + super().command(path)


def html_to_pdf():
    html = "<h2>HTML TO PDF<h3>"
    path_dir = '/tmp/temp.pdf'
    HeadlessPdfKit(html,'string').to_pdf(path_dir)

html_to_pdf()
