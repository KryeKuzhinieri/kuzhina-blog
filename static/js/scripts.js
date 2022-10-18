function documentScroller() {
 /* var h = document.documentElement;*/
	/*var b = document.body;*/
	/*var st = 'scrollTop';*/
	/*var sh = 'scrollHeight';*/
	/*var scroll;*/
	/*var progress = document.querySelector('#progress');*/
	/*var scrollpos = window.scrollY;*/
	/*var header = document.getElementsByTagName("header")[0];*/
	/*var navcontent = document.getElementById("nav-content");*/

	/*document.addEventListener('scroll', function() {*/
		/*[>Refresh scroll % width<]*/
		/*scroll = (h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight) * 100;*/
		/*progress.style.setProperty('--scroll', scroll + '%');*/
		/*[>Apply classes for slide in bar<]*/
		/*scrollpos = window.scrollY;*/
		/*if (scrollpos > 10) {*/
			/*header.classList.add("shadow");*/
		/*} else {*/
			/*header.classList.remove("shadow");*/
		/*}*/
	/*});*/
}

document.addEventListener("DOMContentLoaded", function() {
    var themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
    var themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');

    // Change the icons inside the button based on previous settings
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        themeToggleLightIcon.classList.remove('hidden');
    } else {
        themeToggleDarkIcon.classList.remove('hidden');
    }

    var themeToggleBtn = document.getElementById('theme-toggle');

    themeToggleBtn.addEventListener('click', function() {

        // toggle icons inside button
        themeToggleDarkIcon.classList.toggle('hidden');
        themeToggleLightIcon.classList.toggle('hidden');

        // if set via local storage previously
        if (localStorage.getItem('color-theme')) {
            if (localStorage.getItem('color-theme') === 'light') {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            }

        // if NOT set via local storage previously
        } else {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            }
        }
        
    });

});

