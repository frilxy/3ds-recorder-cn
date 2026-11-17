#include "i18n.h"

#include <stdio.h>
#include <string.h>
#include <strings.h>

static const char *const EN[S_COUNT] = {
#define X(id, en, uk) [id] = en,
    STRINGS(X)
#undef X
};
static const char *const UK[S_COUNT] = {
#define X(id, en, uk) [id] = uk,
    STRINGS(X)
#undef X
};

/* i18n_zh.c: the Simplified Chinese column, one designated initializer per key. */
extern const char *const I18N_ZH[S_COUNT];

static const char *const *const TABLE[LANG_COUNT] = {[LANG_EN] = EN, [LANG_UK] = UK, [LANG_ZH] = I18N_ZH};

/* The Chinese build starts in Chinese; upstream starts in English and switches like before. */
static const Lang DEFAULT_LANG =
#ifdef CN_BUILD
    LANG_ZH;
#else
    LANG_EN;
#endif

static Lang g_lang = DEFAULT_LANG;

Lang i18n_default(void) { return DEFAULT_LANG; }

void i18n_set_language(Lang lang) { g_lang = (unsigned)lang < LANG_COUNT ? lang : LANG_EN; }
Lang i18n_language(void) { return g_lang; }

Lang i18n_next(Lang lang) { return (Lang)(((unsigned)lang + 1) % LANG_COUNT); }

const char *i18n_tag(Lang lang)
{
    switch (lang) {
    case LANG_UK: return "uk";
    case LANG_ZH: return "zh";
    default: return "en";
    }
}

Lang i18n_from_tag(const char *tag)
{
    if (tag && strcasecmp(tag, "uk") == 0)
        return LANG_UK;
    if (tag && strcasecmp(tag, "zh") == 0)
        return LANG_ZH;
    return LANG_EN;
}

const char *T(Str id)
{
    if ((unsigned)id >= S_COUNT)
        return "";
    const char *const *table = TABLE[g_lang];
    /* a key the Chinese table missed falls back to English rather than to nothing */
    return (table && table[id]) ? table[id] : EN[id];
}

const char *i18n_recordings(unsigned n, char *buf, unsigned cap)
{
    if (g_lang == LANG_ZH)
        snprintf(buf, cap, "%u 个录像", n);
    else if (g_lang == LANG_EN)
        snprintf(buf, cap, n == 1 ? "%u recording" : "%u recordings", n);
    else {
        const unsigned d = n % 10, dd = n % 100;
        const char *w = d == 1 && dd != 11 ? "запис" : d >= 2 && d <= 4 && (dd < 12 || dd > 14) ? "записи" : "записів";
        snprintf(buf, cap, "%u %s", n, w);
    }
    return buf;
}
