args <- commandArgs(trailingOnly = TRUE)
t <- as.double(args)
cat("the time is now ",as.character(Sys.time()),'\n')
cat("zzzzzz",'\n')
Sys.sleep(t)
cat("hello - I slept for ",t," seconds",'\n')
cat("the time is now ",as.character(Sys.time()),'\n')