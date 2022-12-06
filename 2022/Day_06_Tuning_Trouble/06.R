#!/usr/bin/env Rscript

require(readr)

args <- commandArgs(trailingOnly = T)
if (length(args) != 1) {
	cat("usage: 06.R INPUT")
	quit()
}

data <- read_lines(args[1])

for (i in 4:(nchar(data)-4)) {
	if (length(unique(strsplit(substr(data, i, i+3),"")[[1]])) == 4) {
		cat("First marker at: ", i+3)
		break
	}
}
