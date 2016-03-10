# videojs-popquiz

This plugin provides the ability to display of pop quizzes over
the [videojs](https://github.com/videojs/video.js) player.

## Usage

Initialize the `popquiz` plugin like the following:

```
  videojs('player_id', {
    plugins: {
      popquiz: {
        'src': "provide the url to the data",
        'data': "or provide the data directly",
        'tracker': "url of backend to report results (optional)",
        'yolo': true/false # get only one chance to answer
      }
    }
  }
```

## Data Parameters

```
  'data': [
    {
      'id': 1,
      'time': 10,
      'question': 'Please select the odd numbers',
      'options': [
        ['1', true],
        ['2', false],
        ['9', true],
        ['11', true],
        ['banana', false]
      ]
    },
    {
      'id': 'over-9000'
      'time': 80,
      'question': '1 + 1 = 2',
      'options': [
        ['true', true],
        ['false', false],
        ['neither', false]
      ]
    }
  ]
```
