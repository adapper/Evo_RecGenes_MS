## GOAL

## pdf		: Generate main text.
.PHONY : pdf
pdf : DapperPayseur_2018.pdf 

DapperPayseur_2018.pdf : DapperPayseur_2018.md
	pandoc -V geometry:margin=1in $^ -fmarkdown-implicit_figures -s -o $@

## clean		: Remove auto-generated files.
.PHONY : clean
clean : 
	rm -f *.pdf

## help		: Print help documentation.
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
