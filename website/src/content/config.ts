export const languages = ["en", "ru", "ar", "zh"] as const;
export type Language = typeof languages[number];
