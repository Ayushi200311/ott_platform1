document.addEventListener("DOMContentLoaded", function () {
  const toggleBtn = document.getElementById('menu-toggle');
  const dropdown = document.getElementById('profile-dropdown');
  const darkToggle = document.getElementById('darkModeToggle');

  // 🌙 Load theme from localStorage
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('dark');
    darkToggle.checked = true;
  } else {
    document.body.classList.add('light');
    darkToggle.checked = false;
  }

  // 📌 Toggle dropdown
  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation(); 
    dropdown.classList.toggle('show');
  });

  document.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target) && e.target !== toggleBtn) {
      dropdown.classList.remove('show');
    }
  });

  // 🌗 Theme toggle switch
  darkToggle.addEventListener('change', () => {
    if (darkToggle.checked) {
      document.body.classList.remove('light');
      document.body.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      document.body.classList.remove('dark');
      document.body.classList.add('light');
      localStorage.setItem('theme', 'light');
    }
  });
});
