#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = T)
if (length(args) != 1) {
	cat("usage: 06.R INPUT")
	quit()
}

data <- read.table(args[1])[[1]][1]

found.marker <- F
for (i in 4:(nchar(data)-4)) {
	if (!found.marker & length(unique(strsplit(substr(data, i, i+3),"")[[1]])) == 4) {
		cat("First marker at: ", i+3, "\n")
		found.marker <- T
	}
	if (length(unique(strsplit(substr(data, i, i+13),"")[[1]])) == 14) {
		cat("Message marker at: ", i+13, "\n")
		break
	}

}

