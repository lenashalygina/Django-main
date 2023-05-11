from django.shortcuts import render

def view(request):
    data = {
        'navbar': '<nav>Navbar content</nav>',
        'footer': '<footer>Footer content</footer>',
        'main': '<section>Main content</section>',
        'base': 'https://example.com',
        'title': 'My Website',
        'filter': 'filter applied'
    }
    return render(request, 'template.html', data)
