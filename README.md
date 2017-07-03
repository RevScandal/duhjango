Global Domination Via Data URLs and The File Reader Api.....The Super Easy Way.


* The css file, styles.css

```css
		body {text-align: center;} 
		
		img { width:23em;margin:2em;border-radius:1em}			
		
		video { height:90%;margin:2em;border-radius:1em}			
		
		textarea {margin:2em;border-radius:1em;padding:3em; text-align: left;}			
			
		form {width: 21em;border:thin solid gray; border-radius: .2em; padding:.5em;font-size: 1.3em; text-align: justify;}	
			
		form, textarea {background: #e0e0e0;}		
```

## Data Url As Image Source

* The html

```html

<!DOCTYPE html>
<html>
	<head>
		<title> Data Url As Image Source</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="styles.css"> 
	</head>
	<body>
		<form>
				<input  type="file">	
		</form>
		<img/>
	
	</body>
	<script src="1.js">
</script>
</html>

```

* The JavaScript file, 1.js

```javascript

		// Get A reference to an element and clear it's value
		function elInit(eltag){
			var el=document.getElementsByTagName(eltag)[0];
			el.value="";
			return el	
			}
			
		// When a onload event fires for the image file, 
		// set the img element src attribute to the data url	
		function showImage(evt){
		//evt.target.result is the image data url
			document.getElementsByTagName("img")[0].src=evt.target.result;
		}
	
	  // when the file input element value changes,
		// read the file as a data url
		function process(evt){
			var file = inFile.files[0];
			var r=new FileReader();
				//when the file loads in the reader, 
			//fire an event to call the showImage function
			r.onload=showImage;
			r.readAsDataURL(file);
		}
   
		var inFile=elInit("input");
		inFile.onchange=process
```

###  Data Url As Video Source

	

### The html

```html

<!DOCTYPE html>
<html>
	<head>
		<title> Data Url As Video Source </title>
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
	<script src="2.js"> </script>

</html>

```

### The JavaScript file, 2.js

```javascript
		// Get A reference to an element and clear it's value
		function elInit(eltag){
			var el=document.getElementsByTagName(eltag)[0];
			el.value="";
			return el	
			}
	
		function playVid(evt){
			var vid=document.getElementsByTagName("video")[0];
			vid.onerror=vid.stop;
			var media=evt.target.result;
				vid.controls=true;
				vid.src=media;
				vid.play();
		}
	
	  // when the file input element value changes,
		// fire an event and read the file as a data url		
		function process(evt){
			var file = inFile.files[0];
			var r=new FileReader();
			//when the file loads in the reader, 
			//fire an event to call the playVid function
			r.onload=playVid;
			r.readAsDataURL(file);
		}


		var inFile=elInit("input");
		inFile.onchange=process
```

##  Read File As Text 


### The html

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
		<script src="3.js"> </script>

</html>
```


### The JavaScript file, 3.js

```javascript

		// Display the file as text in the text area element		
		function showText(evt){
			textArea.value=evt.target.result;
		}
		
		// Get A reference to an element and clear it's value
		function elInit(eltag){
			var el=document.getElementsByTagName(eltag)[0];
			el.value="";
			return el	
			}
			
		// when the file input element value changes,
		// fire an event and read the file as text	
		function process(evt){
			var file = inFile.files[0];
			var r=new FileReader();
			r.onload=showText;
			r.readAsText(file);
		}
   
		var textArea=elInit("textarea");
		var inFile=elInit("input");
		inFile.onchange=process
```
		
