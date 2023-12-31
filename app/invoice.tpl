<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8" />
  <title>Invoice</title>
</head>

<body>
  <div class="container">
    <div class="logo-container">
      <img style="height: 18px" src="https://app.useanvil.com/img/email-logo-black.png">
    </div>

    <table class="invoice-info-container">
      <tr>
        <td rowspan="2" class="client-name"></td>
        <td>
          山田 太郎 様
        </td>
      </tr>
      <tr>
        <td></td>
      </tr>
      <tr>
        <td>
          請求日: <strong>{{ invoice_date }}</strong>
        </td>
        <td></td>
      </tr>
      <tr>
        <td>
          請求書番号: <strong>{{ invoice_number }}</strong>
        </td>
        <td></td>
      </tr>
    </table>


    <table class="line-items-container">
      <thead>
        <tr>
          <th class="heading-quantity">数量</th>
          <th class="heading-description">商品名</th>
          <th class="heading-price">単価</th>
          <th class="heading-subtotal">小計</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>2</td>
          <td>Blue large widgets</td>
          <td class="right">$15.00</td>
          <td class="bold">$30.00</td>
        </tr>
        <tr>
          <td>4</td>
          <td>Green medium widgets</td>
          <td class="right">$10.00</td>
          <td class="bold">$40.00</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Red small widgets with logo</td>
          <td class="right">$7.00</td>
          <td class="bold">$35.00</td>
        </tr>
      </tbody>
    </table>


    <table class="line-items-container has-bottom-border">
      <thead>
        <tr>
          <th>Payment Info</th>
          <th>Due By</th>
          <th>Total Due</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="payment-info">
            <div>
              Account No: <strong>123567744</strong>
            </div>
            <div>
              Routing No: <strong>120000547</strong>
            </div>
          </td>
          <td class="large">May 30th, 2024</td>
          <td class="large total">$105.00</td>
        </tr>
      </tbody>
    </table>

    <div class="footer">
      <div class="footer-info">
        <span>hello@useanvil.com</span> |
        <span>555 444 6666</span> |
        <span>useanvil.com</span>
      </div>
      <div class="footer-thanks">
        <img src="https://github.com/anvilco/html-pdf-invoice-template/raw/main/img/heart.png" alt="heart">
        <span>Thank you!</span>
      </div>
    </div>
  </div>
</body>

</html>