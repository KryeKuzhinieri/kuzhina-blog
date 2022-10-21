function documentScroller() {
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
    scroll = (h[st] || b[st]) / ((h[sh] || b[sh]) - h.clientHeight) * 100;
    progress.style.setProperty('--scroll', scroll + '%');
    scrollpos = window.scrollY;
    if (scrollpos > 10) {
      header.classList.add("shadow");
    } else {
      header.classList.remove("shadow");
    }
  });
}

function loadedTheme() {
    // On page load or when changing themes, best to add inline in `head` to avoid FOUC
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        switchEditorTheme("dark")
    } else {
        document.documentElement.classList.remove('dark')
        switchEditorTheme("light")
    }
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
                switchEditorTheme("dark")
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
                switchEditorTheme("light")
            }

        // if NOT set via local storage previously
        } else {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
                switchEditorTheme("light")
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
                switchEditorTheme("dark")
            }
        }
        
    });

});


function LoadCSS( cssURL ) {
    // 'cssURL' is the stylesheet's URL, i.e. /css/styles.css
    return new Promise( function( resolve, reject ) {
        var link = document.createElement( 'link' );
        link.rel  = 'stylesheet';
        link.href = cssURL;
        document.head.appendChild( link );
        link.onload = function() { 
            resolve(); 
        };
    } );
}


function switchEditorTheme(theme) {
  var path = "/static/ckeditor/ckeditor/plugins/codesnippet/lib/highlight/styles/"
  if (theme == "dark") {
    var editorTheme = document.querySelector('link[href*="default.css"]');
    console.log(editorTheme)
    if (editorTheme != null) editorTheme.parentNode.removeChild(editorTheme)
    LoadCSS(path + "zenburn.css")
  } else {
    var editorTheme = document.querySelector('link[href*="solarized_dark.css"]');
    if (editorTheme != null) editorTheme.parentNode.removeChild(editorTheme)
    LoadCSS(path + "magula.css")
  }
}
