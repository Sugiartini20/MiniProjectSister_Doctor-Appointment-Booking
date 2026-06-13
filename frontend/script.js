// Data dokter
const doctors = [
    { id: 1, name: "dr. Budi Santoso, Sp.PD", specialty: "Penyakit Dalam", experience: "12 tahun", icon: "👨‍⚕️" },
    { id: 2, name: "dr. Ani Wijaya, Sp.A", specialty: "Anak", experience: "8 tahun", icon: "👩‍⚕️" },
    { id: 3, name: "dr. Citra Dewi, Sp.KJ", specialty: "Psikiatri", experience: "10 tahun", icon: "👩‍⚕️" }
];

let selectedDoctor = null;
let lastBookingData = null; // Simpan data booking terakhir

// Render list dokter
function renderDoctorList() {
    const container = document.getElementById('doctorListContainer');
    if (!container) return;

    container.innerHTML = doctors.map(doc => `
        <div class="doctor-item" onclick="selectDoctor(${doc.id})" data-doctor-id="${doc.id}">
            <div class="doctor-avatar">${doc.icon}</div>
            <div class="doctor-info">
                <h4>${doc.name}</h4>
                <p>${doc.specialty} • ${doc.experience}</p>
            </div>
        </div>
    `).join('');
}

// Pilih dokter
function selectDoctor(id) {
    selectedDoctor = doctors.find(d => d.id === id);
    
    // Update UI
    document.querySelectorAll('.doctor-item').forEach(item => {
        item.classList.remove('selected');
        if (item.getAttribute('data-doctor-id') == id) {
            item.classList.add('selected');
        }
    });
    
    // Update hidden input
    const hiddenInput = document.getElementById('selectedDoctorId');
    if (hiddenInput) hiddenInput.value = id;
}

// Booking function
async function processBooking() {
    const patientName = document.getElementById('patientName')?.value;
    const tanggal = document.getElementById('tanggal')?.value;
    const jam = document.getElementById('jam')?.value;
    
    // Validasi
    if (!patientName || !selectedDoctor || !tanggal || !jam) {
        showNotification('❌ Semua field harus diisi!', 'error');
        return;
    }
    
    // Tampilkan loading
    const btn = document.querySelector('.btn-primary');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<div class="spinner" style="width:20px;height:20px;"></div> Memproses...';
    btn.disabled = true;
    
    try {
        const response = await fetch("http://127.0.0.1:5000/booking", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                patient_name: patientName,
                doctor_id: selectedDoctor.id
            })
        });
        
        const data = await response.json();
        
        // Simpan data booking terakhir
        lastBookingData = {
            patient_name: patientName,
            doctor_name: selectedDoctor.name,
            doctor_specialty: selectedDoctor.specialty,
            tanggal: tanggal,
            jam: jam,
            queue_number: data.queue_number || Math.floor(Math.random() * 20) + 1
        };
        
        // Tampilkan notifikasi dengan tombol "Lihat Detail"
        showNotificationWithDetail(lastBookingData);
        
    } catch (error) {
        showNotification('❌ Booking gagal. Silakan coba lagi.', 'error');
    } finally {
        btn.innerHTML = originalText;
        btn.disabled = false;
    }
}

// Tampilkan notifikasi dengan tombol Lihat Detail
function showNotificationWithDetail(bookingData) {
    const container = document.getElementById('notificationContainer');
    if (!container) return;
    
    container.innerHTML = `
        <div class="notification-box" style="background: #d4edda; border-left-color: #28a745;">
            <div style="color: #155724; font-weight: 500; margin-bottom: 12px;">
                ✅ Booking berhasil! Nomor antrean: #${bookingData.queue_number}
            </div>
            <button onclick="goToDetail()" style="
                background: #28a745;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
                font-size: 14px;
                font-weight: 600;
                width: 100%;
            ">
                📋 Lihat Detail Booking
            </button>
        </div>
    `;
}

// Tampilkan notifikasi biasa (error/info)
function showNotification(message, type = 'info') {
    const container = document.getElementById('notificationContainer');
    if (!container) return;
    
    const bgColor = type === 'success' ? '#d4edda' : (type === 'error' ? '#f8d7da' : '#fff3cd');
    const textColor = type === 'success' ? '#155724' : (type === 'error' ? '#721c24' : '#856404');
    
    container.innerHTML = `
        <div class="notification-box" style="background: ${bgColor}; border-left-color: ${type === 'success' ? '#28a745' : (type === 'error' ? '#dc3545' : '#ffc107')}">
            <div style="color: ${textColor}; font-weight: 500;">${message}</div>
        </div>
    `;
}

// Pindah ke halaman detail
function goToDetail() {
    if (lastBookingData) {
        localStorage.setItem("bookingDetail", JSON.stringify(lastBookingData));
    }
    window.location.href = "detail.html";
}

// Initialize saat halaman load
document.addEventListener('DOMContentLoaded', () => {
    renderDoctorList();
    
    // Set default tanggal = hari ini
    const today = new Date().toISOString().split('T')[0];
    const tanggalInput = document.getElementById('tanggal');
    if (tanggalInput) tanggalInput.value = today;
});