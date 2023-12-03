const year = document.getElementById('year');
const month = document.getElementById('month');
const day = document.getElementById('day');
const make = document.getElementById('make');
const calendar = document.getElementById('calendar');

make.addEventListener('click', function() {
    const y = Number(year.value);
    const m = Number(month.value) - 1;
    const d = Number(day.value);
    const date = new Date(y, m, d);
    const startDay = new Date(y, m, 1);
    const endDay = new Date(y, m + 1, 0);
    const startDate = startDay.getDay();
    const endDate = endDay.getDate();
    let dayCount = 1;
    let calendarHtml = '';
    for (let i = 0; i < 6; i++) {
        calendarHtml += '<tr>';
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < startDate) {
                calendarHtml += '<td></td>';
            } else if (dayCount > endDate) {
                calendarHtml += '<td></td>';
            } else if (dayCount === d) {
                calendarHtml += '<td class="today">' + dayCount + '</td>';
            } else {
                calendarHtml += '<td>' + dayCount + '</td>';
            }
            dayCount++;
        }
        calendarHtml += '</tr>';
    }
    calendar.innerHTML = calendarHtml;
});
