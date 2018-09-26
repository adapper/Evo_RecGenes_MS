## GOAL

## pdf		: Generate main text.
.PHONY : pdf
pdf : DapperPayseur_2018.pdf 

DapperPayseur_2018.pdf : DapperPayseur_2018.md References.bib
	pandoc -V geometry:margin=1in --filter=pandoc-citeproc --biblio=References.bib --csl=genetics.csl $< -fmarkdown-implicit_figures -s -o $@

## word		: Generate main text - Word Document.
.PHONY : word
word : DapperPayseur_2018.docx

DapperPayseur2018.docx : DapperPayseur_2018.md References.bib
	pandoc --filter=pandoc-citeproc --biblio=References.bib --csl=genetics.csl $< -fmarkdown-implicit_figures -S -o $@

## info		: Generate pdf.
.PHONY : info
info : Gene_Info/Gene_Info.pdf

Gene_Info/Gene_Info.pdf : Gene_Info/Gene_Info.md References.bib
	pandoc -V geometry:margin=1in --filter pandoc-citeproc $< --bibliography=References.bib -fmarkdown-implicit_figures -s -o $@

## clean		: Remove auto-generated files.
.PHONY : clean
clean : 
	rm -f *.pdf

## help		: Print help documentation.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
