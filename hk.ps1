$i = 0
while($true){
    $r = Get-Random -Minimum 0 -Maximum 2
    $r2 = Get-Random -Minimum 0 -Maximum 2
    $b = ($r -eq 0)
    $b2 = ($r2 -eq 0)
    if($b){Write-Host "Hiragana" -NoNewline}else{Write-Host "Katakana" -NoNewline}
    if($b2){Write-Host ' "'}else{Write-Host ""}
    if($i -gt 100){break}
    $i++
    Read-Host " "
}