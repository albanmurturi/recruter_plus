function toggleUserMenuDropdown() {
    var dropdown = document.getElementById('user-menu-dropdown');
    dropdown.classList.toggle('hidden');
}

// Close dropdown when clicking outside of it
document.addEventListener('click', function (event) {
    var isClickInside = document.getElementById('user-menu').contains(event.target) ||
        document.getElementById('user-menu-dropdown').contains(event.target);

    if (!isClickInside) {
        document.getElementById('user-menu-dropdown').classList.add('hidden');
    }
});