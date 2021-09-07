#mr tic tac toe
mrttt<-c("       XXXXXXXXXXXXXXXXXXXXXX", "    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX", 
         "  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", " XXXXXXXXXXXXXXXXXX         XXXXXXXX", 
         "XXXXXXXXXXXXXXXX              XXXXXXX", "XXXXXXXXXXXXX                   XXXXX", 
         " XXX     _________ _________     XXX      ", "  XX    I  _xxxxx I xxxxx_  I    XX        ", 
         " ( X----I         I         I----X )           ", "( +I    I      00 I 00      I    I+ )", 
         " ( I    I    __0  I  0__    I    I )      /\\    /\\    |\"\"\")  -------  -------  -------", 
         "  (I    I______ /   \\_______I    I)      /  \\  /  \\   |___)     |   __   |   __   |", 
         "   I           ( ___ )           I      /    \\/    \\  |   \\ *   |        |        |", 
         "   I    _  :::::::::::::::  _    I           ", "    \\    \\___ ::::::::: ___/    /          ", 
         "     \\_      \\_________/      _/", "       \\        \\___/        /", 
         "         \\                 /", "          |\\             /|", 
         "          |  \\_________/  |")

# values of board and function to print the board
bval<-c(1,2,3,4,5,6,7,8,9)

board<- function(){
  cat("\n       |       |\n")
  cat(paste("  ",bval[1], "  |  ",bval[2],"  |  ",bval[3]))
  cat('\n_______|_______|_____')
  cat("\n       |       |\n")
  cat(paste("  ",bval[4], "  |  ",bval[5],"  |  ",bval[6]))
  cat('\n_______|_______|_____')
  cat("\n       |       |\n")
  cat(paste("  ",bval[7], "  |  ",bval[8],"  |  ",bval[9]))
  cat("\n       |       |\n")
}

#function to input the values from user without error
input_value<- function(string){
  if (interactive()) {
    con <- stdin()
  } else {
    con <- "stdin"
  }
  cat(string)
  symbol <- readLines(con=con,n=1)
  return (symbol)
}

#make the menu input name and X/O choice give the other choice to cpu
menus<- function(){
  i<-0
  cat(mrttt, sep = "\n")
  cat("WELCOME PLAYER!!! I am Mr. Tic Tac Toe \nShall we play some TIC TAC TOE? \n")
  playername<-input_value("What is your name challenger ? \n")
  while (i==0){
    xno<-input_value(c(playername,", Select your mark: X or O \n"))
    if (xno!="X" & xno!= "O") {
      cat("\n Wrong input! Try Again! \n")
      next
    }else if (xno=="X"){
      human<-"X"
      cpu<-"O"
      i<-1
    }else if(xno=="O"){
      human<-"O"
      cpu<-"X"
      i<-1
    }
      
  }
  return (list(playername=playername, human=human,cpu= cpu))
}
menu_val<-menus()
playername<-  menu_val$playername
human<- menu_val$human
cpu<-  menu_val$cpu
board()
#function to input human move and place it
marking<- function(){
  j<-0
  while (j==0){
      move=input_value(c("\nEnter your move ",playername,", type the number where you want to mark. \n"))
      move<-tryCatch(as.numeric(move),
                    error= function(e){
                      FALSE
                    },
                    warning= function(w){
                      FALSE
                    })
      if(move==FALSE){
        cat("\nWrong Input!!! Try Again \n")
      }else if(is.numeric(move)){
        if (move>=1 & move<10){
          if (bval[move]!='X' & bval[move]!='O'){
            bval[move]<<-human
            j<-1
          }else{
            cat("Position already taken, try different position!")
          }
        }else{
          cat("\nWrong Input!!! Try Again \n")
        }
      }
  }
    board()
}

#to check after and before every move if anyone wins
checkwin<- function(){
  wld<-list(c(1,2,3),c(4,5,6),c(7,8,9),c(1,4,7),c(2,5,8),c(3,6,9),c(1,5,9),c(7,5,3))
  hc<-c(human, cpu)
  win <- FALSE
  winner<-''
  for (seq in wld){
    for (play in hc){
      x<-0
      for (block in seq){
        if (bval[block]==play){
          x<-x+1
        } else next
      }
      if (x==3){ 
        win<-T
        winner<- play
        return (c(win, winner))
      }else next
    }
  }
  return (c(win, winner))
}

#two functions cpucheckh() and cpucheckc() for cpu to read the board, compare values, ck represents a board with numbers which add up to 15 [8,3,4,1,5,9,6,7,2] represents [1,2,3,4,5,6,7,8,9] positions in vertical, horizontal or diagonals,
#checks if human or cpu can win in the next move, returns the positions to play for cpu in such condition. 
cpucheckh<- function(){
  check<-rbind(c(1,2,3),c(4,5,6),c(7,8,9),c(1,4,7),c(2,5,8),c(3,6,9),c(1,5,9),c(7,5,3))
  ck<-rbind(c(8,3,4),c(1,5,9),c(6,7,2),c(8,1,6),c(3,5,7),c(4,9,2),c(8,5,2),c(6,5,4))
  hs<-0
  for (x in 1:8){
    h<-0
    kh<-0
    for (y in 1:3){
      if (bval[check[x,y]]==  human){
        h<-h+1
        kh<-ck[x,y]+kh
      }else if (bval[check[x,y]]==  cpu){
        h<-0
        break
      }else next
    }
    if (h==2){
      hs<-15-kh
      return (c(h,hs))
    }else next
  }
    return (c(0,0))
}
cpucheckc<- function(){
  check<-rbind(c(1,2,3),c(4,5,6),c(7,8,9),c(1,4,7),c(2,5,8),c(3,6,9),c(1,5,9),c(7,5,3))
  ck<-rbind(c(8,3,4),c(1,5,9),c(6,7,2),c(8,1,6),c(3,5,7),c(4,9,2),c(8,5,2),c(6,5,4))
  cs<-0
  for (x in 1:8){
    c<-0
    kc<-0
    for (y in 1:3){
      if (bval[check[x,y]]==  cpu){
        c<-c+1
        kc<-ck[x,y]+kc
      }else if (bval[check[x,y]]==  human){
        c<-0
        break
      }else next
    }
    if (c==2){
      cs<-15-kc
      return (c(c,cs))
    }else next
  }
  return (c(0,0))
}
#function for cpu to mark it's fav position
cpumarking<- function(term,a,b){
  cat("\nMy move\n")
  indexs<-c(8,3,4,1,5,9,6,7,2)
  hum<-cpucheckh()
  cp<-cpucheckc()
  if (cp[1]==2){
    index<- which(indexs == cp[2])[[1]]
    if (bval[index]!=  human & bval[index]!=  cpu){
      bval[index]<<- cpu
      board()
      return (c(a,b)) 
    }
  }else if (hum[1]==2){
    index<- which(indexs == hum[2])[[1]]
    if (bval[index]!=  human & bval[index]!=  cpu){
      bval[index]<<- cpu
      board()
      return (c(a,b))
    }
  }
  # even term for X ,odd for O
  if (term==1 | term==8){
    a<-cpu18()
  }else if (term==2){
    a <- cpu2() 
  }else if (term==3){
    c<-cpu3(a)
    a<-c[1]
    b<-c[2]
  }else if (term==4 | term==6){
    c<-cpu46(a)
    a<-c[1]
    b<-c[2]
  }else if (term==5){
    a<-cpu5(a) 
  }else if (term==7){
    c <- cpu7(a,b)
    a<-c[1]
    b<-c[2]
  }else {
    a <- cpurand()
  }
  board()
  return (c(a,b))
}

# functions which mark for respective term accordingly
cpu18<- function(){
  arr<- c(1,3,7,9)
  for (a in 1:4){
    if (bval[arr[a]]!= human & bval[arr[a]]!=  cpu){
      bval[arr[a]]<<- cpu
      return (a)     
    }else next
  }
  c<-cpurand()
  a<-c[1]
  b<-c[2]
  return (a)
}
  
cpu2<- function(){
  if (bval[5]!= human & bval[5]!=  cpu){
    bval[5]<<- cpu
    return (1)
  }else {
    a <-cpu18()
    return (a)
  }
}

cpu3<- function(a){
  arr<-rbind(c(7,3),c(9,1),c(1,9),c(7,3))
  for (b in 1:2){
    if (bval[arr[a,b]]!= human & bval[arr[a,b]]!=  cpu){
      bval[arr[a,b]]<<-cpu
      return (c(a,b))
    }else next
  }
  c<- cpurand()
  return (c)
}
cpu46<- function(a){
  arr<-rbind(c(8,6),c(4,8),c(2,6),c(4,2))
  if (bval[5]== cpu){
    for (c in 1:4){
      for (b in 1:2){
        if (bval[arr[c,b]]!= human & bval[arr[c,b]]!=  cpu){
          bval[arr[c,b]]<<- cpu
          return (c(c,b)) 
        }else next
      }
    }
  }else{
    for (b in 1:2){
      if (bval[arr[a,b]]!=  human & bval[arr[a,b]]!=  cpu){
        bval[arr[a,b]]<<- cpu
        return (c(a,b))
      }else next
    }
  }
  c<- cpurand()
  return (c)
}
  
cpu5<- function(a){
  arr<-c(9,7,3,1)
  if (bval[arr[a]]!=  human & bval[arr[a]]!=  cpu){
    bval[arr[a]]<<- cpu
    return (a)
  }else{
    c<- cpurand()
    a<-c[1]
    b<-c[2]
    return (a)
  }
}

cpu7<- function(a,b){
  arr<- rbind(c(4,2),c(6,2),c(4,8),c(8,6))
  if (bval[5]!=  human & bval[5]!=  cpu){
    bval[5]<<-cpu
    return (c(a,b))
  }else if (bval[arr[a,b]]!=  human & bval[arr[a,b]]!=  cpu){
    bval[arr[a,b]]<<-  cpu
    return (c(a,b))
  }else {
    c <- cpurand()
    return (c)
  }
}

# a function to mark randomly if the conditions are not fav for cpu
cpurand<- function(){
  arr<- sample(1:9, 9, replace=FALSE)
  for(x in arr){
    if (bval[x]!= human & bval[x]!= cpu){
      bval[x]<<- cpu
      return (c(1,1))
    }else next
  }
}
  
ai=1
bi=1
#loop to play the game, marking() and cpumarking(), check for winner at start of each loop
for (i in 1:9){
  win<-checkwin()
  if (win[1]){
    break
  }else if ( human=='X' & i%%2!=0){
    marking()
  }else if ( human=='O' & i%%2==0){
    marking()
  }else{
    ci<-cpumarking(i,ai,bi)
    ai<-ci[1]
    bi<-ci[2]
  }
  }
win<-checkwin()
if (win[1]){
  cat(paste(win[2]," won!!\n"))
}
if (win[2]==  human){
  board()
  cat(paste("This time you won ", playername ,", you won't be lucky next time."))
}else if(win[2]== cpu){
  board()
  cat("Know your place human, I am a superior being.")
}
# for the draw
if (win[1]==FALSE & i==9){
  cat("It is a draw. You were a worthy challenger ", playername)
  
}
  
