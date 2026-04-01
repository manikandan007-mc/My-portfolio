// script.js
document.addEventListener('DOMContentLoaded', () => {

    // 1. Current Year for Footer
    document.getElementById('year').textContent = new Date().getFullYear();

    // 2. Custom Cursor (only on non-touch devices)
    const cursor = document.querySelector('.cursor');

    if (window.matchMedia("(pointer: fine)").matches) {
        document.addEventListener('mousemove', (e) => {
            cursor.style.left = e.clientX + 'px';
            cursor.style.top = e.clientY + 'px';
        });

        // Add hover effect for links and buttons
        const hoverElements = document.querySelectorAll('a, button, .btn');
        hoverElements.forEach(el => {
            el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
            el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
        });
    }

    // 3. Navbar scroll effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 4. Mobile Menu Toggle
    const mobileBtn = document.getElementById('mobile-btn');
    const navLinks = document.getElementById('nav-links');
    const navLinksItems = document.querySelectorAll('.nav-link');

    mobileBtn.addEventListener('click', () => {
        mobileBtn.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });

    // Close mobile menu when clicking a link
    navLinksItems.forEach(item => {
        item.addEventListener('click', () => {
            mobileBtn.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // 5. Scroll Reveal Animation Setup using IntersectionObserver
    const revealElements = document.querySelectorAll('.reveal');

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // Handle sections individually to stagger children more easily if needed
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        const reveals = section.querySelectorAll('.reveal');
        if (reveals.length > 0) {
            const sectionObserver = new IntersectionObserver((entries, observer) => {
                if (entries[0].isIntersecting) {
                    reveals.forEach((el, index) => {
                        setTimeout(() => {
                            el.classList.add('active');
                        }, index * 100);
                    });
                    observer.unobserve(section);
                }
            }, { threshold: 0.1 });
            sectionObserver.observe(section);
        }
    });

    // Trigger initial check for hero and top elements
    setTimeout(() => {
        const heroReveals = document.querySelectorAll('#hero .reveal');
        heroReveals.forEach((el, index) => {
            setTimeout(() => {
                el.classList.add('active');
            }, index * 150);
        });
    }, 100);

    // Trigger on load for elements already in viewport
    setTimeout(() => {
        revealElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight) {
                el.classList.add('active');
            }
        });
        // 6. Back to Top Button Visibility
        const backToTop = document.getElementById('backToTop');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                backToTop.classList.add('visible');
            } else {
                backToTop.classList.remove('visible');
            }
        });

        // 7. Project & Resume Modal Logic
        const projectModal = document.getElementById('projectModal');
        const modalTitle = document.getElementById('modalTitle');
        const modalDesc = document.getElementById('modalDesc');
        const modalImageContainer = document.getElementById('modalImageContainer');
        const modalImage = document.getElementById('modalImage');
        const modalButton = document.getElementById('modalButton');
        const modalDownload = document.getElementById('modalDownload');
        const closeModal = document.getElementById('closeModal');
        const projectCards = document.querySelectorAll('.project-card');
        const resumeBtn = document.getElementById('resumeBtn');

        const openModal = (title, type, content) => {
            modalTitle.textContent = title;
            
            if (type === 'project') {
                modalDesc.style.display = 'block';
                modalImageContainer.style.display = 'none';
                modalButton.style.display = 'inline-block';
                modalDownload.style.display = 'none';
                modalButton.setAttribute('href', content);
            } else if (type === 'resume') {
                modalDesc.style.display = 'none';
                modalImageContainer.style.display = 'block';
                modalImage.setAttribute('src', content);
                modalButton.style.display = 'none';
                modalDownload.style.display = 'inline-block';
            }
            
            projectModal.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            // Success reset scroll
            const container = projectModal.querySelector('.modal-container');
            if(container) container.scrollTop = 0;
        };

        projectCards.forEach(card => {
            card.addEventListener('click', (e) => {
                e.preventDefault();
                const title = card.querySelector('.project-title').textContent;
                const link = card.getAttribute('data-link');
                if (link) openModal(title, 'project', link);
            });
        });

        if (resumeBtn) {
            resumeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                const src = resumeBtn.getAttribute('data-src');
                if (src) openModal('Professional Resume', 'resume', src);
            });
        }

        if (closeModal) {
            closeModal.addEventListener('click', () => {
                projectModal.classList.remove('active');
                document.body.style.overflow = '';
            });
        }

        // Close on click outside the modal box
        if (projectModal) {
            projectModal.addEventListener('click', (e) => {
                if (e.target === projectModal) {
                    projectModal.classList.remove('active');
                    document.body.style.overflow = '';
                }
            });
        }

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && projectModal.classList.contains('active')) {
                projectModal.classList.remove('active');
                document.body.style.overflow = '';
            }
        });



        // 9. Project Card Hover Glow Effect
        const cards = document.querySelectorAll('.project-card');
        cards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                
                const glow = card.querySelector('.project-card-glow');
                if (glow) {
                    glow.style.setProperty('--x', `${x}px`);
                    glow.style.setProperty('--y', `${y}px`);
                }
            });
        });

    }, 100);

});
