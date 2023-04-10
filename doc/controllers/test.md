# Test

```python
test_controller = client.test
```

## Class Name

`TestController`

## Methods

* [Languages](../../doc/controllers/test.md#languages)
* [Detect](../../doc/controllers/test.md#detect)
* [Translate](../../doc/controllers/test.md#translate)


# Languages

Returns a list of supported languages for translation.

```python
def languages(self)
```

## Response Type

`mixed`

## Example Usage

```python
result = test_controller.languages()
print(result)
```

## Example Response

```
{
  "data": {
    "languages": [
      {
        "language": "af"
      },
      {
        "language": "ak"
      },
      {
        "language": "am"
      },
      {
        "language": "ar"
      },
      {
        "language": "as"
      },
      {
        "language": "ay"
      },
      {
        "language": "az"
      },
      {
        "language": "be"
      },
      {
        "language": "bg"
      },
      {
        "language": "bho"
      },
      {
        "language": "bm"
      },
      {
        "language": "bn"
      },
      {
        "language": "bs"
      },
      {
        "language": "ca"
      },
      {
        "language": "ceb"
      },
      {
        "language": "ckb"
      },
      {
        "language": "co"
      },
      {
        "language": "cs"
      },
      {
        "language": "cy"
      },
      {
        "language": "da"
      },
      {
        "language": "de"
      },
      {
        "language": "doi"
      },
      {
        "language": "dv"
      },
      {
        "language": "ee"
      },
      {
        "language": "el"
      },
      {
        "language": "en"
      },
      {
        "language": "eo"
      },
      {
        "language": "es"
      },
      {
        "language": "et"
      },
      {
        "language": "eu"
      },
      {
        "language": "fa"
      },
      {
        "language": "fi"
      },
      {
        "language": "fr"
      },
      {
        "language": "fy"
      },
      {
        "language": "ga"
      },
      {
        "language": "gd"
      },
      {
        "language": "gl"
      },
      {
        "language": "gn"
      },
      {
        "language": "gom"
      },
      {
        "language": "gu"
      },
      {
        "language": "ha"
      },
      {
        "language": "haw"
      },
      {
        "language": "he"
      },
      {
        "language": "hi"
      },
      {
        "language": "hmn"
      },
      {
        "language": "hr"
      },
      {
        "language": "ht"
      },
      {
        "language": "hu"
      },
      {
        "language": "hy"
      },
      {
        "language": "id"
      },
      {
        "language": "ig"
      },
      {
        "language": "ilo"
      },
      {
        "language": "is"
      },
      {
        "language": "it"
      },
      {
        "language": "iw"
      },
      {
        "language": "ja"
      },
      {
        "language": "jv"
      },
      {
        "language": "jw"
      },
      {
        "language": "ka"
      },
      {
        "language": "kk"
      },
      {
        "language": "km"
      },
      {
        "language": "kn"
      },
      {
        "language": "ko"
      },
      {
        "language": "kri"
      },
      {
        "language": "ku"
      },
      {
        "language": "ky"
      },
      {
        "language": "la"
      },
      {
        "language": "lb"
      },
      {
        "language": "lg"
      },
      {
        "language": "ln"
      },
      {
        "language": "lo"
      },
      {
        "language": "lt"
      },
      {
        "language": "lus"
      },
      {
        "language": "lv"
      },
      {
        "language": "mai"
      },
      {
        "language": "mg"
      },
      {
        "language": "mi"
      },
      {
        "language": "mk"
      },
      {
        "language": "ml"
      },
      {
        "language": "mn"
      },
      {
        "language": "mni-Mtei"
      },
      {
        "language": "mr"
      },
      {
        "language": "ms"
      },
      {
        "language": "mt"
      },
      {
        "language": "my"
      },
      {
        "language": "ne"
      },
      {
        "language": "nl"
      },
      {
        "language": "no"
      },
      {
        "language": "nso"
      },
      {
        "language": "ny"
      },
      {
        "language": "om"
      },
      {
        "language": "or"
      },
      {
        "language": "pa"
      },
      {
        "language": "pl"
      },
      {
        "language": "ps"
      },
      {
        "language": "pt"
      },
      {
        "language": "qu"
      },
      {
        "language": "ro"
      },
      {
        "language": "ru"
      },
      {
        "language": "rw"
      },
      {
        "language": "sa"
      },
      {
        "language": "sd"
      },
      {
        "language": "si"
      },
      {
        "language": "sk"
      },
      {
        "language": "sl"
      },
      {
        "language": "sm"
      },
      {
        "language": "sn"
      },
      {
        "language": "so"
      },
      {
        "language": "sq"
      },
      {
        "language": "sr"
      },
      {
        "language": "st"
      },
      {
        "language": "su"
      },
      {
        "language": "sv"
      },
      {
        "language": "sw"
      },
      {
        "language": "ta"
      },
      {
        "language": "te"
      },
      {
        "language": "tg"
      },
      {
        "language": "th"
      },
      {
        "language": "ti"
      },
      {
        "language": "tk"
      },
      {
        "language": "tl"
      },
      {
        "language": "tr"
      },
      {
        "language": "ts"
      },
      {
        "language": "tt"
      },
      {
        "language": "ug"
      },
      {
        "language": "uk"
      },
      {
        "language": "ur"
      },
      {
        "language": "uz"
      },
      {
        "language": "vi"
      },
      {
        "language": "xh"
      },
      {
        "language": "yi"
      },
      {
        "language": "yo"
      },
      {
        "language": "zh"
      },
      {
        "language": "zh-CN"
      },
      {
        "language": "zh-TW"
      },
      {
        "language": "zu"
      }
    ]
  }
}
```


# Detect

Detects the language of text within a request.

```python
def detect(self,
          q,
          content_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `q` | `string` | Form, Required | The input text upon which to perform language detection. |
| `content_type` | `string` | Header, Required | defining content type as x-www-form-urlencoded |

## Response Type

`mixed`

## Example Usage

```python
q = 'English is hard, but detectably so'

content_type = 'application/x-www-form-urlencoded'

result = test_controller.detect(
    q,
    content_type
)
print(result)
```

## Example Response

```
{
  "data": {
    "detections": [
      [
        {
          "confidence": 1,
          "isReliable": false,
          "language": "en"
        }
      ]
    ]
  }
}
```


# Translate

Translates input text, returning translated text

```python
def translate(self,
             q,
             target)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `q` | `string` | Form, Required | The input text to translate |
| `target` | `string` | Form, Required | target language to translate the text to |

## Response Type

`mixed`

## Example Usage

```python
q = 'Hello, world!'

target = 'es'

result = test_controller.translate(
    q,
    target
)
print(result)
```

## Example Response

```
{
  "data": {
    "translations": [
      {
        "translatedText": "¡Hola Mundo!"
      }
    ]
  }
}
```

