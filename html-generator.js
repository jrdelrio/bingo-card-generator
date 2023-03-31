import fs


const files = fs.readdirSync('.')
              .filter(file => fs.statSync(file).isFile())
              .map(file => ({ name: file, size: fs.statSync(file).size }));

console.log(files);


// fetch('data.csv')
//   .then(response => response.text())
//   .then(csvText => {
//     const csv = require('csv-parse/lib/sync');
//     const records = csv(csvText, {columns: true});
//     const values = records.map(record => record.value);
//     const html = generateHtml(values);
//     return html;
//   });

// function generateHtml(values) {
//   const tableRows = values.map(value => `<tr><td>${value}</td></tr>`);
//   const html = `
//     <html>
//       <body>
//         <table>
//           ${tableRows.join('\n')}
//         </table>
//       </body>
//     </html>
//   `;
//   return html;
// }