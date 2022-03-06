# Module Wrapper Function

- Node.js는 모듈을 로드하기 전에, `Module Wrapper Function`이라는 것으로 모듈 내의 전체 코드를 감싸주는 작업을 진행

## Module Wrapper Function

- 모듈을 감싸주는 코드(Module Wrapper Function)
  ```js
  (function (exports, require, module, __filename, __dirname) {
    //모듈 코드
  });
  ```
- math-tools.js 모듈 로드 시
  ```js
  (function (exports, require, module, __filename, __dirname) {
    function add(a, b) {
      return a + b;
    }
  exports.add = add;
  });
  ```
  - Module Wrapper Function의 다섯가지 인자(exports, require, module, __filename, __dirname)에 Node.js가 각각 알맞은 것들을 전달해줌
  - 따라서 우리가 직접 정의해준 적이 없더라도, 모듈 안에서 항상 자유롭게 접근 가능

## Module Wrapper Function 출력

- console.dir : 특정 객체의 내부 속성들을 모두 출력하는 함수

- exports 없는 코드 (외부 공개X)
  - math-tools.js
    ```js
    function add(a, b) {
      return a + b;
    }

    console.log('exports -------------------------------------------->');
    console.dir(exports);
    console.log('require -------------------------------------------->');
    console.dir(require);
    console.log('module -------------------------------------------->');
    console.dir(module);
    console.log('__filename -------------------------------------------->');
    console.dir(__filename);
    console.log('__dirname -------------------------------------------->');
    console.dir(__dirname);
    ```
  - 결과
    ```cmd
    PS C:\codeit\nodeStudy> node .\math-tools.js
    exports -------------------------------------------->
    {} ⭐
    require -------------------------------------------->       
    [Function: require] {
      resolve: [Function: resolve] { paths: [Function: paths] },
      main: Module {
        id: '.',
        path: 'C:\\codeit\\nodeStudy',
        exports: {}, 
        filename: 'C:\\codeit\\nodeStudy\\math-tools.js',
        loaded: false,
        children: [],
        paths: [
          'C:\\codeit\\nodeStudy\\node_modules',
          'C:\\codeit\\node_modules',
          'C:\\node_modules'
        ]
      },
      extensions: [Object: null prototype] {
        '.js': [Function (anonymous)],
        '.json': [Function (anonymous)],
        '.node': [Function (anonymous)]
      },
      cache: [Object: null prototype] {
        'C:\\codeit\\nodeStudy\\math-tools.js': Module {
          id: '.',
          path: 'C:\\codeit\\nodeStudy',
          exports: {},
          filename: 'C:\\codeit\\nodeStudy\\math-tools.js',
          loaded: false,
          children: [],
          paths: [Array]
        }
      }
    }
    module -------------------------------------------->
    Module {
      id: '.',
      path: 'C:\\codeit\\nodeStudy',
      exports: {}, ⭐
      filename: 'C:\\codeit\\nodeStudy\\math-tools.js',
      loaded: false,
      children: [],
      paths: [
        'C:\\codeit\\nodeStudy\\node_modules',
        'C:\\codeit\\node_modules',
        'C:\\node_modules'
      ]
    }
    __filename -------------------------------------------->
    'C:\\codeit\\nodeStudy\\math-tools.js'
    __dirname -------------------------------------------->
    'C:\\codeit\\nodeStudy'
    ```
    - 'exports 객체'와 'module 객체의 exports 프로퍼티가 가리키는 객체'는 **동일한 객체**임!
    - 모듈 내부의 것들을 외부로 공개하기 위해 `exports`나 `module.exports`를 쓰는 것은 바로 이 객체에 접근하기 위함임

- exports 있는 코드 (외부 공개O)
  - math-tools.js
    ```js
    function add(a, b) {
      return a + b;
    }

    // add함수를 plus라는 이름으로 공개
    exports.plus = add;

    console.log('exports -------------------------------------------->');
    console.dir(exports);
    console.log('require -------------------------------------------->');
    console.dir(require);
    console.log('module -------------------------------------------->');
    console.dir(module);
    console.log('__filename -------------------------------------------->');
    console.dir(__filename);
    console.log('__dirname -------------------------------------------->');
    console.dir(__dirname);
    ```
  - 결과
    ```cmd
    PS C:\codeit\nodeStudy> node .\math-tools.js
    exports -------------------------------------------->
    { plus: [Function: add] } ⭐
    require -------------------------------------------->       
    [Function: require] {
      resolve: [Function: resolve] { paths: [Function: paths] },
      main: Module {
        id: '.',
        path: 'C:\\codeit\\nodeStudy',
        exports: { plus: [Function: add] },
        filename: 'C:\\codeit\\nodeStudy\\math-tools.js',       
        loaded: false,
        children: [],
        paths: [
          'C:\\codeit\\nodeStudy\\node_modules',
          'C:\\codeit\\node_modules',
          'C:\\node_modules'
        ]
      },
      extensions: [Object: null prototype] {
        '.js': [Function (anonymous)],
        '.json': [Function (anonymous)],
        '.node': [Function (anonymous)]
      },
      cache: [Object: null prototype] {
        'C:\\codeit\\nodeStudy\\math-tools.js': Module {
          id: '.',
          path: 'C:\\codeit\\nodeStudy',
          exports: [Object],
          filename: 'C:\\codeit\\nodeStudy\\math-tools.js',
          loaded: false,
          children: [],
          paths: [Array]
        }
      }
    }
    module -------------------------------------------->
    Module {
      id: '.',
      path: 'C:\\codeit\\nodeStudy',
      exports: { plus: [Function: add] }, ⭐
      filename: 'C:\\codeit\\nodeStudy\\math-tools.js',
      loaded: false,
      children: [],
      paths: [
        'C:\\codeit\\nodeStudy\\node_modules',
        'C:\\codeit\\node_modules',
        'C:\\node_modules'
      ]
    }
    __filename -------------------------------------------->
    'C:\\codeit\\nodeStudy\\math-tools.js'
    __dirname -------------------------------------------->
    'C:\\codeit\\nodeStudy'
    ``
    - exports 객체에 'plus'라는 프로퍼티가 추가되고, 프로퍼티의 값이 'add 함수'로 설정됨
    - module 객체의 exports 프로퍼티도 동일한 객체를 가리킴(= 다른 모듈에 공개하고 싶은 것들이 모인 객체)
    - ⭐이 객체가 다른 모듈에서 require 함수로 로드할 때 리턴되는 객체임⭐

## 정리 및 주의

- 정리
  - exports.속성 = 값 ⭕
  - module.exports = 객체 ⭕
- 주의
  - exports = 객체 ❌
    - Node.js는 내부적으로 require 함수가 실행될 때, 'module 객체의 exports 프로퍼티가 가리키는 객체'를 리턴하도록 설계됨 (exports 객체 X)
    - 만약 위 코드로 exports 객체를 아예 새로 설정해버리면, 더 이상 exports 키워드로는 원래의 객체에 접근할 수 없게 됨!
    - 따라서 exports 키워드로는 `exports.속성 = 값`처럼 해당 객체에 프로퍼티를 추가하는 식으로만 사용 가능
    - cf) module 키워드는 `module.exports = 객체`와 `module.exports.속성 = 값` 모두 가능