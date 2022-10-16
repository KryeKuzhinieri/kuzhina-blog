function documentScroller() {
	console.log('test----')	
	var h = document.documentElement;
	var b = document.body;
	var st = 'scrollTop';
	var sh = 'scrollHeight';
	var scroll;
	var progress = document.querySelector('#progress');
	var scrollpos = window.scrollY;
	var header = document.getElementsByTagName("header")[0];
	var navcontent = document.getElementById("nav-content");

	document.addEventListener('scroll', function() {
		/*Refresh scroll % width*/
		scroll = (h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight) * 100;
		progress.style.setProperty('--scroll', scroll + '%');
		/*Apply classes for slide in bar*/
		scrollpos = window.scrollY;
		if (scrollpos > 10) {
			header.classList.add("shadow");
		} else {
			header.classList.remove("shadow");
		}
	});
}
