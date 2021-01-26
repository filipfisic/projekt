def fun_korisnici(podaci):

    string = '''<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>KORISNICI</h2>

<table>
  <tr>
    <th>Korsnik</th>
  </tr>
  '''
    for i in range(len(podaci)):
        string = string + '''<tr>
    <td>''' + podaci[i] + '''</td>
  </tr>'''
    string = string + '''
  </tr>
</table>

</body>
</html>

'''
    return string
