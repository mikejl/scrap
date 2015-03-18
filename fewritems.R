# ##############################################
# fewritems.R
# Few R Items
# Mike Libassi
# March 2015
# ##############################################

# ####################### Set working dir #######
dir <- '/home/mike/R'
setwd(dir)

# ####################### Turn off Scientific Notation ########
options(scipen = 999) 


# ######################### Trim blanks #######################
trim <- function (x) gsub("^\\s+|\\s+$", "", x)

# #############  Start / end of month function ################
# Start som(som(Sys.Date()) - 1) End = som(Sys.Date()) - 1  ###
som <- function(x) {
  as.Date(format(x, "%Y-%m-01"))
}

# ####################### Previous Month #####################
sdate <- som(som(Sys.Date()) - 1)
edate <- som(Sys.Date()) - 1

# ####################### Format for SAS query ###############
startd <- paste0("'",format(sdate,'%d%b%Y'),"'d")
endd <- paste0("'",format(edate,'%d%b%Y'),"'d")
