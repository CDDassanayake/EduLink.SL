# Stripe Test Card Details for Development

## Test Card Numbers

Use these test card numbers with Stripe in test mode (no real charges):

### Successful Payments
- **Card Number:** `4242 4242 4242 4242`
- **Expiry:** Any future date (e.g., `12/34`)
- **CVC:** Any 3 digits (e.g., `123`)
- **ZIP:** Any 5 digits (e.g., `12345`)

### Requires Authentication
- **Card Number:** `4000 0025 0000 3155`
- **Expiry:** Any future date
- **CVC:** Any 3 digits
- **ZIP:** Any 5 digits

### Card Declined
- **Card Number:** `4000 0000 0000 0002`
- **Expiry:** Any future date
- **CVC:** Any 3 digits
- **ZIP:** Any 5 digits

### Insufficient Funds
- **Card Number:** `4000 0012 6000 0000`
- **Expiry:** Any future date
- **CVC:** Any 3 digits
- **ZIP:** Any 5 digits

## Important Notes

1. **Test Mode Only:** These cards only work when Stripe is in test mode
2. **No Real Charges:** No money is actually charged when using these cards
3. **Test API Keys:** Ensure you're using Stripe test keys (starting with `sk_test_` and `pk_test_`)
4. **Webhook Testing:** For webhook testing, use Stripe CLI or the Stripe Dashboard webhook testing feature

## Setting Up Stripe Test Mode

1. Go to [Stripe Dashboard](https://dashboard.stripe.com/)
2. Toggle "Test mode" in the top right corner
3. Copy your test API keys from "Developers" > "API keys"
4. Add them to your `.env` file:
   ```
   STRIPE_SECRET_KEY=sk_test_...
   STRIPE_PUBLISHABLE_KEY=pk_test_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   ```

## Webhook Testing

To test webhooks locally:
1. Install Stripe CLI: `npm install -g stripe`
2. Login: `stripe login`
3. Forward webhooks: `stripe listen --forward-to localhost:8000/api/v1/payments/webhook`
4. Copy the webhook secret from the CLI output and add to your `.env`

## Production vs Test

- **Test Mode:** Use test cards, no real money, test API keys
- **Production Mode:** Use real cards, real charges, live API keys
- **Never use test cards in production**
- **Never use live API keys in development**
