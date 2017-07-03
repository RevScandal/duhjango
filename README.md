## Show Data Url Image

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

# Play Data Url Video

```html 
<!DOCTYPE html>
<html>
	<head>
		<title> Play Data Url Video </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
			<link rel="stylesheet" href="styles.css"> 
	</head>
	<body>
		<form>
				<input type="file">	
		</form>
		<video>
		</video>
	</body>
	<script>
	
		function parseMime(media){
			var mimetype= media.split(":")[1].split(";")[0]
			return mimetype
		}

		function playVid(evt){
			var vid= document.querySelector("video")
			var media=evt.target.result
			var mimetype=parseMime(media)
			if (vid.canPlayType(mimetype)){
				vid.controls=true
				vid.src=media
				vid.play()
			}
		}
	
		function pullFile(evt){
			var file = inFile.files[0]
			var r=new FileReader()
			r.onload=playVid
			r.readAsDataURL(file)
		}

		var inFile=document.querySelector("input")
		inFile.value=""
		inFile.onchange=pullFile

	</script>
</html>
```

## Show File As Data Url
```html
<!DOCTYPE html>
<html>
	<head>
		<title> Show File As Data Url </title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="styles.css"> 
	</head>
	<body>
		<form>
				<input  type="file">	
		</form>	
		<textarea rows="25" cols="80">
		</textarea>
	</body>
	<script>
	
		function showDataUrl(evt){
			textArea.value=String(evt.target.result)
		}

		function pullFile(evt){
			var file = inFile.files[0]
			var r=new FileReader()
			r.onload=showDataUrl
			r.readAsDataURL(file)
		}

		var inFile=document.querySelector("input")
		inFile.value=""
		inFile.onchange=pullFile
		var textArea=document.querySelector("textarea")
		textArea.value=""
	</script>
</html>
```
##  Read File As Text 
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
