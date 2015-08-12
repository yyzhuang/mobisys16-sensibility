notarealfile.pdf: 
	pdflatex mobisys.tex
	pdflatex mobisys.tex
	bibtex mobisys
	pdflatex mobisys.tex
	bibtex mobisys
	pdflatex mobisys.tex
	

clean:
	rm -f mobisys.pdf
	rm -f *.dvi
	rm -f *.toc
	rm -f *.bbl
	rm -f *.aux
	rm -f *.log
	rm -f *.blg
	rm -f *.bak
	rm -f *.out
	rm -f *.ps
