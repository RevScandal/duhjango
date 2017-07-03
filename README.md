* Show Data Url Image

```html
<!DOCTYPE html>
<html>
	<head>
		<title> Show Data Url Image</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="styles.css"> 
	</head>
	<body>
		<form>
				<input  type="file">	
		</form>
		<img>
		</img>
	</body>
	<script>
	
		function showImage(evt){
			document.querySelector("img").src=evt.target.result
		}

		function pullFile(evt){
			var file = inFile.files[0]
			var r=new FileReader()
			r.onload=showImage
			r.readAsDataURL(file)
		}

		var inFile=document.querySelector("input")
		inFile.value=""
		inFile.onchange=pullFile

	</script>
</html>
```
```html
<!DOCTYPE html>
<html>
	<head>
		<title> Read File As Text </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="styles.css"> 
	</head>
	<body>
		<form>
			<input  type="file">	
		</form>
		<textarea rows="15" cols="100">
		</textarea>
	</body>
	<script>

		function showText(evt){
			textArea.value=evt.target.result
		}

		function pullFile(evt){
			var file = inFile.files[0]
			var r=new FileReader()
			r.onload=showText
			r.readAsText(file)
		}
   
		var inFile=document.querySelector("input")
		inFile.value=""
		inFile.onchange=pullFile
		var textArea=document.querySelector("textarea")
		textArea.value=""
	  		
	</script>
</html>
```
