function restoreOriginalNavbarBrand() {
	var originalBrandContent = '';
	document.querySelectorAll('.navbar__brand').forEach(function(element) {
		if (element.hasAttribute('data-original-brand')) {
			originalBrandContent = element.getAttribute('data-original-brand');
		}
	});

	if (originalBrandContent) {
		document.querySelectorAll('.navbar__brand').forEach(function(element) {
			element.parentNode.removeChild(element);
		});
		var restoredBrand = document.createElement('a');
		restoredBrand.classList.add('navbar__brand');
		restoredBrand.innerHTML = originalBrandContent;
		restoredBrand.setAttribute('href', '/');
		var navbarItems = document.querySelector('.navbar__items');
		navbarItems.insertBefore(restoredBrand, navbarItems.firstChild);
	}
}

function checkNavbarBrandValid() {
	if (document.querySelector('#continue_reading_buttons') && !document.querySelector('#continue_reading')) {
		restoreOriginalNavbarBrand();
	}
}

function confirm(text, callback) {
    restoreOriginalNavbarBrand();  // Ensure any existing added elements are removed before adding new ones
	
    var brand = document.querySelector('.navbar__brand');

    var question = document.createElement('div');
    question.classList.add('navbar__brand');
    question.setAttribute('data-original-brand', brand.innerHTML);
    question.setAttribute('id', "continue_reading");
    question.innerHTML = text;
    brand.parentNode.insertBefore(question, brand);
    brand.style.display = 'none';

    var buttons = document.createElement('div');
    buttons.classList.add('navbar__brand');
    buttons.setAttribute('id', "continue_reading_buttons");
    buttons.setAttribute('data-original-brand', brand.innerHTML);
    buttons.innerHTML = '<button class="button button--primary" style="margin-right:5px;">Yes</button><button class="button button--secondary">No</button>';
    brand.parentNode.insertBefore(buttons, brand);
    buttons.querySelector('button').addEventListener('click', function() {
        restoreOriginalNavbarBrand();
        callback(true);
    });
    buttons.querySelector('button:last-child').addEventListener('click', function() {
        restoreOriginalNavbarBrand();
        callback(false);
    });

    var oldHref = window.location.href;
    setInterval(function() {
        if (oldHref !== window.location.href) {
            oldHref = window.location.href;
			checkNavbarBrandValid();
        }
    }, 100);
}

var loadedScroll = false;

function getCurrentPage() {
    let currentPage = document.URL.split("https://nanosyste.ms/")[1].split("#")[0];
    if (currentPage.endsWith("/")) {
        currentPage = currentPage.slice(0, -1);
    }
    return currentPage;
}

function onDocumentReady(og = true) {
    if (document.URL != 'https://nanosyste.ms/') {
        let currentPage = getCurrentPage();
        let lastScroll = localStorage.getItem("nanosystems-scroll-page_" + currentPage);
        if (document.URL.includes("#continue")) {
            document.documentElement.scrollTop = lastScroll;
        } else if (lastScroll && lastScroll > 150) {
            confirm("Continue reading?", function(continueReading) {
                if (continueReading) {
                    currentPage = getCurrentPage();
                    lastScroll = localStorage.getItem("nanosystems-scroll-page_" + currentPage);
                    document.documentElement.scrollTop = lastScroll;
                }
            });
        }
        if (!loadedScroll) {
            window.addEventListener('scroll', function() {
                let currentPage = getCurrentPage();
                if (currentPage == '') return;
                localStorage.setItem("nanosystems-scroll-page_" + currentPage, document.documentElement.scrollTop);
                localStorage.setItem("nanosystems-last-page", currentPage);
            });
        }
    }

    if (document.URL == 'https://nanosyste.ms/') {
        let lastPage = localStorage.getItem("nanosystems-last-page");
        if (lastPage && lastPage !== 'undefined') {
            confirm("Continue reading?", function(continueReading) {
                if (continueReading) {
                    if (lastPage === undefined) {
                        lastPage = localStorage.getItem("nanosystems-last-page");
                    }
                    if (lastPage != 'undefined') {
                        window.location.href = 'https://nanosyste.ms/' + lastPage + '#continue';
                    }
                }
            });
        }
    }

    if (og) {
        var oldHref = window.location.href;
        setInterval(function() {
            if (oldHref != window.location.href) {
                oldHref = window.location.href;
                onDocumentReady(false);
            }
        }, 100);
		
		// Constantly check if there are buttons and no continue_reading
		setInterval(function() {
			checkNavbarBrandValid();
		}, 100);
    }
}

if (document.readyState === 'loading' || document.readyState === 'interactive') {
    document.addEventListener('load', function() {
        setTimeout(onDocumentReady, 200);
    });
} else {
    setTimeout(onDocumentReady, 200);
}
