'use strict';

const locationSelectBox = document.querySelector("#location-select-box");
locationSelectBox.addEventListener('click', showLocationCheckboxes);

const identitySelectBox = document.querySelector("#identity-select-box");
identitySelectBox.addEventListener('click', showIdentityCheckboxes);

const typeSelectBox = document.querySelector("#type-select-box");
typeSelectBox.addEventListener('click', showTypeCheckboxes);

function showLocationCheckboxes() {
    const locationCheckboxes = document.querySelector("#location-checkbox-group");
    if (locationCheckboxes.classList.contains('show')) {
        locationCheckboxes.classList.remove('show');
    } else {
        locationCheckboxes.classList.add('show');
    }
}

function showIdentityCheckboxes() {
    const identityCheckboxes = document.querySelector("#identity-checkbox-group");
    if (identityCheckboxes.classList.contains('show')) {
        identityCheckboxes.classList.remove('show');
    } else {
        identityCheckboxes.classList.add('show');
    }
}

function showTypeCheckboxes() {
    const typeCheckboxes = document.querySelector("#type-checkbox-group");
    if (typeCheckboxes.classList.contains('show')) {
        typeCheckboxes.classList.remove('show');
    } else {
        typeCheckboxes.classList.add('show');
    }
}