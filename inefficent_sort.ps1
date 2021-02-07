#long sort
#provided an array of numbers sort inefficently.

function inefficent-sort1{
    param(
        $arr
    )


    Write-Host -NoNewline "Array: "
    foreach($i in $arr){
        Write-Host -NoNewline "$i,"
    }
    Write-Host ""
    $t = 0
    while($true){
        $t++
        $arr = $arr | Sort-Object { Get-Random }
        
        #check the array if in order
        $ch = $true
        foreach($i in 1..($arr.Count -1)){
            if($ch){
                $ch = ($arr[$i-1] -le $arr[$i])
            }
        }
        if($ch){    #if in order
            Write-Host -NoNewline "Sorted: "
            foreach($i in $arr){
                Write-Host -NoNewline "$i,"
            }
            Write-Host ""
            Write-Host "Iterations: $t" 
            break
        }
        if($t -ge (1000 * 1000)){     #if over a million
            Write-Host -NoNewline "Array: "
            foreach($i in $arr){
                Write-Host -NoNewline "$i,"
            }
            Write-Host ""
            Write-Host "**Failed to Iterate in Time**"
            break
        }
    }
}

function inefficent-sort2{
    param(
        $arr
    )

    $t=0
    while($true){
        $t++
        #if smaller than first put in first and move everything to right
        #else contiune
        $r = Get-Random -Minimum 1 -Maximum ($arr.Count-1)
        if($arr[0] -le $arr[$r]){
            $tp = $arr[0]
            $arr[0] = $arr[$r]
            
            foreach($q in 2..($arr.Count-1)){
                $tp2 = $arr[$q]
                $arr[$q] = $arr[$q-1]
                $arr[$q-1] = $tp2
            }
        } 



        #check the array if in order
        $ch = $true
        foreach($i in 1..($arr.Count -1)){
            if($ch){
                $ch = ($arr[$i-1] -le $arr[$i])
            }
        }
        if($ch){    #if in order
            Write-Host -NoNewline "Sorted: "
            foreach($i in $arr){
                Write-Host -NoNewline "$i,"
            }
            Write-Host ""
            Write-Host "Iterations: $t" 
            break
        }
        if($t -ge (1000 * 1000)){     #if over a million
            Write-Host -NoNewline "Array: "
            foreach($i in $arr){
                Write-Host -NoNewline "$i,"
            }
            Write-Host ""
            Write-Host "**Failed to Iterate in Time**"
            break
        }
    }
}


#-----------------------------------------------
#intialize array
$array = @(0)*8
foreach($i in 0..($array.Count -1)){
    $array[$i] = Get-Random -Maximum 100
}
#-----------------------------------------------

inefficent-sort1 -arr $array

Write-Host -NoNewline "Array: "
foreach($i in $arr){
    Write-Host -NoNewline "$i,"
}
Write-Host ""
