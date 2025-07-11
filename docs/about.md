# About

The S2GOS example application demonstrates how to bring the S2GOS scene generator and observation simulator into the S2GOS service architecture.

## Development

The S2GOS example application uses [pixi](https://pixi.sh/dev/) to manage the project. You can install the development environemnt using

```bash
pixi install -e dev
```

A local service can be started using

```bash
pixi run dev
```

or

```bash
s2gos-server dev --service=s2gos_example_app.app:service
```

The client can be tested in `./notbook/client-api.ipynb`.

### Code Style

The source code is formatted and quality-controlled
using [ruff](https://docs.astral.sh/ruff/):

```bash
ruff format
ruff check
```

## License

The S2GOS example application is open source made available under the terms and conditions of the
[Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).
