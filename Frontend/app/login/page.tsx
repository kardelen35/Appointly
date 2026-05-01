export default function LoginPage() {
  return (
    <main className="min-h-screen bg-background flex items-center justify-center px-4 py-8">
      <section className="relative w-full max-w-[390px] overflow-hidden rounded-[2rem] border border-border bg-card px-8 py-10 shadow-xl">
        {/* soft background shapes */}
        <div className="absolute -right-16 -top-16 h-40 w-40 rounded-full bg-secondary/40" />
        <div className="absolute -bottom-20 -left-20 h-44 w-44 rounded-full bg-secondary/40" />

        <div className="relative z-10">
          {/* LOGO */}
          <div className="mb-9 text-center">
  <div className="mx-auto mb-5 flex h-20 w-20 items-center justify-center rounded-full bg-primary/10 shadow-inner">
    <svg
      width="58"
      height="58"
      viewBox="0 0 100 100"
      className="text-primary drop-shadow-sm"
      fill="none"
    >
      <circle cx="50" cy="22" r="11" fill="currentColor" />

      <path
        d="M50 42C31 48 22 64 23 82C40 79 50 65 50 42Z"
        fill="currentColor"
        opacity="0.9"
      />

      <path
        d="M50 42C69 48 78 64 77 82C60 79 50 65 50 42Z"
        fill="currentColor"
        opacity="0.75"
      />

      <path
        d="M50 47C42 61 43 81 50 94C57 81 58 61 50 47Z"
        fill="currentColor"
      />
    </svg>
  </div>

  <h1 className="text-[34px] font-bold leading-none text-primary">
    Log In
  </h1>

  <p className="mt-3 text-sm text-text/70">
   Your Account
  </p>
</div>

          {/* FORM */}
          <form className="space-y-4">
            <input
              type="email"
              placeholder="E-posta veya Telefon"
              className="h-13 w-full rounded-xl border border-border bg-background px-4 text-sm text-text outline-none placeholder:text-text/40 focus:border-primary"
            />

            <input
              type="password"
              placeholder="Şifre"
              className="h-13 w-full rounded-xl border border-border bg-background px-4 text-sm text-text outline-none placeholder:text-text/40 focus:border-primary"
            />

            <div className="text-right">
              <button
                type="button"
                className="text-sm text-primary hover:underline"
              >
                Şifremi unuttum?
              </button>
            </div>

            <button
              type="submit"
              className="h-13 w-full rounded-xl bg-primary font-semibold text-white transition hover:opacity-90"
            >
              Giriş Yap
            </button>
          </form>

          <p className="mt-6 text-center text-sm text-text/70">
            Hesabınız yok mu?{" "}
            <span className="font-semibold text-primary">Kaydolun</span>
          </p>
        </div>
      </section>
    </main>
  );
}