def fun_grupe(x):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  text-align: center;
}

.dropdown {
  position: center;
  text-align: center;
}

.dropdown-content {
  display: none;
  position: center;

  min-width: 36px;

  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}

.dropdown:hover .dropbtn {background-color: #3e8e41;}

div2 {
  margin: auto;
  text-align: center;
  width: 50%;
  padding: 150px;
}
</style>
</head>
<body>
<div2>
<br><br><br><br><br><br><br><br><br><br>
<h2>Odaberite grupu</h2>
<p></p>

<br><br>
<div class="dropdown">
  <button class="dropbtn">Grupa</button>
  <div class="dropdown-content"> '''
    for y in x:
        html = html + '''<a href="''' + '''/grupa/''' + y + '''">''' + y[6:len(y) - 4] + '''</a>'''

    html = html + '''
  </div>
  </div>
</div2>

</body>
</html>
'''

    return html
