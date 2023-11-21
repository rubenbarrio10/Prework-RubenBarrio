#1

salario <- function(coste_hora, horas = 40, retenciones = 0.02){
    if(horas > 45){
        horas_extra = horas - 45
        coste_extra = coste_hora * 1.5
        bruto = (45 * coste_hora) + (horas_extra * coste_extra)
        neto = bruto * (1 - retenciones)
    } else{
        bruto = horas * coste_hora
        neto = bruto * (1 - retenciones)
    }
   return(list("Salario bruto" = bruto, "Salario neto" = neto))
}

salario(20, 50, 0.2)


#2 FOR

media <- function(x){
  resultado <- 0
  for(i in 1:length(x)){
    resultado <- resultado + x[i]
  }
  resultado/length(x)
}

media(1:11)


#3 WHILE

media <- function(x){
    resultado <- 0
    i <- 1
    while(i <= length(x)){
        resultado <- resultado + x[i]
        i <- i + 1
    }
    resultado/length(x)
}

media(20:30)


#4 VECTORIZACIÓN

media <- function(x){
  sum(x)/length(x)
}

media(20:30)