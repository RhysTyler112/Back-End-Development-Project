const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteBookingName = document.getElementById("deleteBookingName");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        const bookingId = button.getAttribute("data-id");
        const bookingName = button.getAttribute("data-name");

        // Update modal content with booking details
        deleteBookingName.textContent = bookingName;

        // Update delete confirmation link
        deleteConfirm.href = `/delete-booking/${bookingId}/`;

        // Show the modal
        deleteModal.show();
    });
}
