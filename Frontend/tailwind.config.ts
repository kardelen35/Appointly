import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./redux/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#F4F4EF",
        primary: "#6B7A5A",
        secondary: "#DAD7CD",
        accent: "#B08968",
        text: "#2C2C2C",
        card: "#FFFDF8",
        border: "#DED8CE",
      },
    },
  },
};

export default config;