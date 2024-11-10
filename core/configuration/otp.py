from decouple import config

# OTP settings
OTP_MAX_LIMIT = config('OTP_MAX_LIMIT', default=30, cast=int)
OTP_INTERVAL_LIMIT = config('OTP_INTERVAL_LIMIT', default=2, cast=int)
OTP_ATTEMPT = config('OTP_ATTEMPT', default=5, cast=int)